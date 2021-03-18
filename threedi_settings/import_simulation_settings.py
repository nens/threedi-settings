from pathlib import Path
import logging

import typer

from threedi_settings.threedimodel_config import ThreedimodelIni
from threedi_settings.api_models import OpenAPINumericalSettings
from threedi_settings.api_models import OpenAPITimeStepSettings
from threedi_settings.api_models import OpenAPIGeneralSettings

logger = logging.getLogger(__name__)


settings_app = typer.Typer()


@settings_app.command()
def import_settings(simulation_id: int, ini_file: Path):
    """
    "Create API V3 settings resources from legacy model ini file"
    """
    mi = ThreedimodelIni(ini_file)
    OpenAPINumericalSettings(simulation_id, mi.as_dict()).create()
    OpenAPITimeStepSettings(simulation_id, mi.as_dict()).create()
    OpenAPIGeneralSettings(simulation_id, mi.as_dict()).create()


if __name__ == "__main__":
    settings_app()

# def main():
#     parser = argparse.ArgumentParser(
#         description="Create API V3 settings resources from legacy model ini file"
#     )
#     parser.add_argument(
#         "ini_files",
#         type=Path,
#         metavar="ini-files",
#         nargs="+",
#         help="path to ini file. Separate multiple files by space, "
#         "e.g one.ini two.ini",
#     )
#
#     args = parser.parse_args()
#     for f in args.ini_files:
#         logger.info("processing %s ", f)
#         import_settings(f)


# if __name__ == "__main__":
#     main()
