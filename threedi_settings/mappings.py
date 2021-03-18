from dataclasses import dataclass
from typing import Any, Tuple, Optional
from typing import Type
from openapi_client.models import AggregationSettings
from openapi_client.models import GeneralSettings
from openapi_client.models import TimeStepSettings
from openapi_client.models import NumericalSettings


@dataclass(frozen=True)
class FieldInfo:
    # prob needs endpoint attribute to be able
    # to post data to correct URL
    name: str
    type: Any


@dataclass(frozen=True)
class FieldInfoOld(FieldInfo):
    pass


@dataclass(frozen=True)
class FieldInfoNew(FieldInfo):
    default: Optional[Any]
    openapi_model: Type


general_settings_map = {
    "use_advection_1d": [
        FieldInfoOld("advection_1d", int),
        FieldInfoNew("use_advection_1d", int, 1, GeneralSettings),
    ],
    "use_advection_2d": [
        FieldInfoOld("advection_2d", int),
        FieldInfoNew("use_advection_2d", int, 1, GeneralSettings),
    ],
}

time_step_settings_map = {
    "time_step": [
        FieldInfoOld("timestep", float),
        FieldInfoNew("time_step", float, 1.0, TimeStepSettings),
    ],
    "min_time_step": [
        FieldInfoOld("minimum_timestep", float),
        FieldInfoNew("min_time_step", float, 0.1, TimeStepSettings),
    ],
    "max_time_step": [
        FieldInfoOld("maximum_timestep", float),
        FieldInfoNew("max_time_step", float, 1.0, TimeStepSettings),
    ],
    "use_time_step_stretch": [
        FieldInfoOld("timestep_plus", bool),
        FieldInfoNew("use_time_step_stretch", bool, False, TimeStepSettings),
    ],
    "output_time_step": [
        FieldInfoOld("output_timestep", float),
        FieldInfoNew("output_time_step", float, 1.0, TimeStepSettings),
    ],
}

# old -> new
numerical_settings_map = {
    # "flow_variable": [FieldInfoOld("flow_variable", str), FieldInfoNew("flow_variable", str, None)],
    # "aggregation_method": [FieldInfoOld("aggregation_method", str), FieldInfoNew("method", str, None)],
    # "timestep": [FieldInfoOld("timestep", float), FieldInfoNew("interval", float, None)],
    "cfl_strictness_factor_1d": [
        FieldInfoOld("cfl_strictness_factor_1d", float),
        FieldInfoNew(
            "cfl_strictness_factor_1d", float, 1.0, NumericalSettings
        ),
    ],
    "cfl_strictness_factor_2d": [
        FieldInfoOld("cfl_strictness_factor_2d", float),
        FieldInfoNew(
            "cfl_strictness_factor_2d", float, 1.0, NumericalSettings
        ),
    ],
    "flow_direction_threshold": [
        FieldInfoOld("flow_direction_threshold", float),
        FieldInfoNew(
            "flow_direction_threshold", float, 1e-05, NumericalSettings
        ),
    ],
    "convergence_cg": [
        FieldInfoOld("convergence_cg", float),
        FieldInfoNew("convergence_cg", float, 1.0e-9, NumericalSettings),
    ],
    "friction_shallow_water_depth_correction": [
        FieldInfoOld("friction_shallow_water_correction", int),
        FieldInfoNew(
            "friction_shallow_water_depth_correction",
            int,
            0,
            NumericalSettings,
        ),
    ],
    "general_numerical_threshold": [
        FieldInfoOld("general_numerical_threshold", float),
        FieldInfoNew(
            "general_numerical_threshold", float, 1.0e-8, NumericalSettings
        ),
    ],
    "time_integration_method": [
        FieldInfoOld("integration_method", int),
        FieldInfoNew("time_integration_method", int, 0, NumericalSettings),
    ],
    "limiter_waterlevel_gradient_1d": [
        FieldInfoOld("limiter_grad_1d", int),
        FieldInfoNew(
            "limiter_waterlevel_gradient_1d", int, 1, NumericalSettings
        ),
    ],
    "limiter_waterlevel_gradient_2d": [
        FieldInfoOld("limiter_grad_2d", int),
        FieldInfoNew(
            "limiter_waterlevel_gradient_2d", int, 1, NumericalSettings
        ),
    ],
    "limiter_slope_crossectional_area_2d": [
        FieldInfoOld("limiter_slope_crossectional_area_2d", int),
        FieldInfoNew(
            "limiter_slope_crossectional_area_2d", int, 0, NumericalSettings
        ),
    ],
    "limiter_slope_friction_2d": [
        FieldInfoOld("limiter_slope_friction_2d", int),
        FieldInfoNew("limiter_slope_friction_2d", int, 0, NumericalSettings),
    ],
    "max_non_linear_newton_iterations": [
        FieldInfoOld("max_nonlinear_iteration", int),
        FieldInfoNew(
            "max_non_linear_newton_iterations", int, 20, NumericalSettings
        ),
    ],
    "max_degree_gauss_seidel": [
        FieldInfoOld("maximum_degree", int),
        FieldInfoNew("max_degree_gauss_seidel", int, 20, NumericalSettings),
    ],
    "min_friction_velocity": [
        FieldInfoOld("minimum_friction_velocity", float),
        FieldInfoNew("min_friction_velocity", float, 0.01, NumericalSettings),
    ],
    "min_surface_area": [
        FieldInfoOld("minimum_surface_area", float),
        FieldInfoNew("min_surface_area", float, 1.0e-8, NumericalSettings),
    ],
    "use_preconditioner_cg": [
        FieldInfoOld("precon_cg", int),
        FieldInfoNew("use_preconditioner_cg", int, 1, NumericalSettings),
    ],
    "preissmann_slot": [
        FieldInfoOld("preissmann_slot", float),
        FieldInfoNew("preissmann_slot", float, 0.0, NumericalSettings),
    ],
    "pump_implicit_ratio": [
        FieldInfoOld("pump_implicit_ratio", float),
        FieldInfoNew("pump_implicit_ratio", float, 1.0, NumericalSettings),
    ],
    "limiter_slope_thin_water_layer": [
        FieldInfoOld("thin_water_layer_definition", float),
        FieldInfoNew(
            "limiter_slope_thin_water_layer", float, 0.01, NumericalSettings
        ),
    ],
    "use_of_cg": [
        FieldInfoOld("use_of_cg", int),
        FieldInfoNew("use_of_cg", int, 20, NumericalSettings),
    ],
    "use_nested_newton": [
        FieldInfoOld("nested_newton", int),
        FieldInfoNew("use_nested_newton", bool, True, NumericalSettings),
    ],
    "flooding_threshold": [
        FieldInfoOld("flooding_threshold", float),
        FieldInfoNew("flooding_threshold", float, 0.000001, NumericalSettings),
    ],
}

settings_map = {
    **general_settings_map,
    **time_step_settings_map,
    **numerical_settings_map,
}