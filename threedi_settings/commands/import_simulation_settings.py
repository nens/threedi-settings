from pathlib import Path
import logging

try:
    import typer
    from rich.console import Console
    from rich.table import Table
except ImportError:
    raise ImportError(
        "You need to install the extra 'cmd', e.g. pip install threedi-settings[cmd]"  # noqa
    )

from threedi_settings.threedimodel_config import ThreedimodelIni
from threedi_settings.threedimodel_config import AggregationIni
from threedi_settings.http.api_clients import OpenAPINumericalSettings
from threedi_settings.http.api_clients import OpenAPITimeStepSettings
from threedi_settings.http.api_clients import OpenAPIGeneralSettings
from threedi_settings.http.api_clients import OpenAPIAggregationSettings
from threedi_settings.http.api_clients import OpenAPISimulationSettings
from threedi_settings.threedimodel_config import ThreedimodelSqlite
from threedi_settings.pretty.output import ResponseTree
from threedi_settings.models import SourceTypes
from typing import Dict, Optional

logger = logging.getLogger(__name__)

settings_app = typer.Typer()


def _create(
    simulation_id: int,
    source: SourceTypes,
    settings: Dict,
    aggregations: Optional[Dict] = None
):
    OpenAPINumericalSettings(simulation_id, settings, source).create()
    OpenAPITimeStepSettings(simulation_id, settings, SourceTypes.sqlite_file).create()
    OpenAPIGeneralSettings(simulation_id, settings, SourceTypes.sqlite_file).create()
    if aggregations:
        OpenAPIAggregationSettings(simulation_id, aggregations).create()
    sim_settings = OpenAPISimulationSettings(simulation_id)
    return sim_settings.retrieve()


@settings_app.command()
def import_from_ini(
    simulation_id: int,
    ini_file: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        writable=False,
        resolve_path=True,
        help="Legacy model settings ini file.",
    ),
    aggregation_file: Path = typer.Argument(
        None,
        exists=True,
        dir_okay=False,
        writable=False,
        resolve_path=True,
        help="Legacy model aggregation settings file.",
    ),
):
    """
    "Create API V3 settings resources from legacy model ini file"
    """
    model_ini = ThreedimodelIni(ini_file)
    aggr = None
    if aggregation_file:
        aggr_ini = AggregationIni(aggregation_file)
        aggr = aggr_ini.as_dict()

    resp = _create(
        simulation_id,
        SourceTypes.ini_file,
        model_ini.as_dict(),
        aggr,
    )
    rt = ResponseTree(resp)
    rt.show()


@settings_app.command()
def import_from_sqlite(
    simulation_id: int,
    sqlite_file: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        writable=False,
        resolve_path=True,
        help="SQLITE model file.",
    ),
    settings_row: int = typer.Argument(
        1,
        help="Specify the row id of the v2_global_settings entry you want to import."
    ),
    aggregations: bool = typer.Option(
        True,
        help=
        "If the '--no-aggregations' option is not explicitlly set, the "
        "aggregation settings found in the sqlite file will be imported, too."
    ),
):
    """
    "Create API V3 settings resources from legacy model sqlite file"
    """

    tms = ThreedimodelSqlite(sqlite_file, settings_row)
    aggr = tms.aggregation_settings if aggregations else None
    resp = _create(
        simulation_id,
        SourceTypes.sqlite_file,
        tms.as_dict(),
        aggr
    )
    rt = ResponseTree(resp)
    rt.show()


if __name__ == "__main__":
    settings_app()
