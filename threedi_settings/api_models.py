# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-
import functools
import logging


from openapi_client.models import GeneralSettings
from openapi_client.models import TimeStepSettings
from openapi_client.models import NumericalSettings

from threedi_settings.mappings import (
    general_settings_map,
    time_step_settings_map,
    numerical_settings_map,
)

logger = logging.getLogger(__name__)

from openapi_client import SimulationsApi
from openapi_client import ApiException
from threedi_api_client import ThreediApiClient
from abc import ABC, abstractmethod


class BaseOpenAPI(ABC):
    def __init__(
        self, simulation_id: int, config_dict, openapi_model, mapping
    ):
        self.simulation_id = simulation_id
        self.config_dict = config_dict
        self.model = openapi_model
        self.mapping = mapping
        _api_client = ThreediApiClient()
        self.api_client = SimulationsApi(_api_client)

    # def convert(self, value, old_type, new_type):
    #     if new_type == bool and old_type == int:
    #         value = old_type(value)
    #         try:
    #             ini_value = new_field_info.type(ini_value)
    #         except Exception:
    #             raise

    @functools.cached_property
    def instance(self):
        data = {}
        exclude = {
            "url",
        }
        for name in self.model.openapi_types.keys():
            if name.lower() in exclude:
                continue
            if name == "simulation_id":
                data[name] = self.simulation_id
                continue
            old_field_info, new_field_info = self.mapping[name]
            ini_value = self.config_dict[old_field_info.name]
            try:
                ini_value = old_field_info.type(ini_value)
                if new_field_info.type != old_field_info.type:
                    try:
                        ini_value = new_field_info.type(ini_value)
                    except Exception:
                        raise
            except ValueError as err:
                logger.warning(f"{err} --> {ini_value} --> {old_field_info}")
                ini_value = new_field_info.default
            data[name] = ini_value
        return self.model(**data)

    @property
    @abstractmethod
    def create_method_name(self) -> str:
        ...

    def create(self):
        try:
            create = getattr(self.api_client, self.create_method_name)
        except AttributeError:
            raise AttributeError(
                f"Create method '{self.create_method_name}' unknown"
            )
        try:
            resp = create(self.simulation_id, self.instance)
        except ApiException as err:
            logger.error(
                "Could not create resource %s. Server response: %s",
                self.model.__name__,
                err,
            )
            return
        logger.info(
            "Successfully created resource %s. Server response: %s ",
            self.model.__name__,
            resp,
        )
        return resp


class OpenAPIGeneralSettings(BaseOpenAPI):
    def __init__(self, simulation_id: int, config):
        super().__init__(
            simulation_id, config, GeneralSettings, general_settings_map
        )

    @property
    def create_method_name(self):
        return "simulations_settings_general_create"


class OpenAPITimeStepSettings(BaseOpenAPI):
    def __init__(self, simulation_id: int, config):
        super().__init__(
            simulation_id, config, TimeStepSettings, time_step_settings_map
        )

    @property
    def create_method_name(self):
        return "simulations_settings_time_step_create"


class OpenAPINumericalSettings(BaseOpenAPI):
    def __init__(self, simulation_id: int, config):
        super().__init__(
            simulation_id, config, NumericalSettings, numerical_settings_map
        )

    @property
    def create_method_name(self):
        return "simulations_settings_numerical_create"
