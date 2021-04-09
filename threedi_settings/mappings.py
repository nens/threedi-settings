from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class FieldInfo:
    name: str
    type: Any


@dataclass(frozen=True)
class FieldInfoIni(FieldInfo):
    ini_section: str


@dataclass(frozen=True)
class FieldInfoSqlite(FieldInfo):
    table_name: str


@dataclass(frozen=True)
class AggregationFieldInfoOld(FieldInfo):
    pass


@dataclass(frozen=True)
class FieldInfoAPI(FieldInfo):
    default: Optional[Any]


general_settings_map = {
    "use_advection_1d": [
        FieldInfoIni("advection_1d", int, "physics"),
        FieldInfoAPI("use_advection_1d", int, 1),
        FieldInfoSqlite("advection_1d", int, "v2_global_settings"),
    ],
    "use_advection_2d": [
        FieldInfoIni("advection_2d", int, "physics"),
        FieldInfoAPI("use_advection_2d", int, 1),
        FieldInfoSqlite("advection_2d", int, "v2_global_settings"),
    ],
}

time_step_settings_map = {
    "time_step": [
        FieldInfoIni("timestep", float, "simulation"),
        FieldInfoAPI("time_step", float, 1.0),
        FieldInfoSqlite("sim_time_step", float, "v2_global_settings"),
    ],
    "min_time_step": [
        FieldInfoIni("minimum_timestep", float, "simulation"),
        FieldInfoAPI("min_time_step", float, 0.1),
        FieldInfoSqlite("minimum_sim_time_step", float, "v2_global_settings"),
    ],
    "max_time_step": [
        FieldInfoIni("maximum_timestep", float, "simulation"),
        FieldInfoAPI("max_time_step", float, 1.0),
        FieldInfoSqlite("maximum_sim_time_step", float, "v2_global_settings"),
    ],
    "use_time_step_stretch": [
        FieldInfoIni("timestep_plus", bool, "numerics"),
        FieldInfoAPI("use_time_step_stretch", bool, False),
        FieldInfoSqlite("timestep_plus", bool, "v2_global_settings"),
    ],
    "output_time_step": [
        FieldInfoIni("output_timestep", float, "output"),
        FieldInfoAPI("output_time_step", float, 1.0),
        FieldInfoSqlite("output_time_step", float, "v2_global_settings"),
    ],
}

# old -> new
numerical_settings_map = {
    "cfl_strictness_factor_1d": [
        FieldInfoIni("cfl_strictness_factor_1d", float, "numerics"),
        FieldInfoAPI("cfl_strictness_factor_1d", float, 1.0),
        FieldInfoSqlite("cfl_strictness_factor_1d", float, "v2_numerical_settings"),
    ],
    "cfl_strictness_factor_2d": [
        FieldInfoIni("cfl_strictness_factor_2d", float, "numerics"),
        FieldInfoAPI("cfl_strictness_factor_2d", float, 1.0),
        FieldInfoSqlite("cfl_strictness_factor_2d", float,
                        "v2_numerical_settings"),
    ],
    "flow_direction_threshold": [
        FieldInfoIni("flow_direction_threshold", float, "numerics"),
        FieldInfoAPI("flow_direction_threshold", float, 1e-05),
        FieldInfoSqlite("flow_direction_threshold", float,
                        "v2_numerical_settings"),
    ],
    "convergence_cg": [
        FieldInfoIni("convergence_cg", float, "numerics"),
        FieldInfoAPI("convergence_cg", float, 1.0e-9),
        FieldInfoSqlite("convergence_cg", float,
                        "v2_numerical_settings"),
    ],
    "friction_shallow_water_depth_correction": [
        FieldInfoIni(
            "friction_shallow_water_correction", int, "physical_attributes"
        ),
        FieldInfoAPI(
            "friction_shallow_water_depth_correction",
            int,
            0,
        ),
        FieldInfoSqlite("frict_shallow_water_correction", int,
                        "v2_numerical_settings"),
    ],
    "general_numerical_threshold": [
        FieldInfoIni("general_numerical_threshold", float, "numerics"),
        FieldInfoAPI("general_numerical_threshold", float, 1.0e-8),
        FieldInfoSqlite("general_numerical_threshold", float,
                        "v2_numerical_settings"),
    ],
    "time_integration_method": [
        FieldInfoIni("integration_method", int, "numerics"),
        FieldInfoAPI("time_integration_method", int, 0),
        FieldInfoSqlite("integration_method", int,
                        "v2_numerical_settings"),
    ],
    "limiter_waterlevel_gradient_1d": [
        FieldInfoIni("limiter_grad_1d", int, "numerics"),
        FieldInfoAPI("limiter_waterlevel_gradient_1d", int, 1),
        FieldInfoSqlite("limiter_grad_1d", int,
                        "v2_numerical_settings"),
    ],
    "limiter_waterlevel_gradient_2d": [
        FieldInfoIni("limiter_grad_2d", int, "numerics"),
        FieldInfoAPI("limiter_waterlevel_gradient_2d", int, 1),
        FieldInfoSqlite("limiter_grad_2d", int,
                        "v2_numerical_settings"),
    ],
    "limiter_slope_crossectional_area_2d": [
        FieldInfoIni("limiter_slope_crossectional_area_2d", int, "numerics"),
        FieldInfoAPI("limiter_slope_crossectional_area_2d", int, 0),
        FieldInfoSqlite("limiter_slope_crossectional_area_2d", int,
                        "v2_numerical_settings"),
    ],
    "limiter_slope_friction_2d": [
        FieldInfoIni("limiter_slope_friction_2d", int, "numerics"),
        FieldInfoAPI("limiter_slope_friction_2d", int, 0),
        FieldInfoSqlite("limiter_slope_friction_2d", int,
                        "v2_numerical_settings"),
    ],
    "max_non_linear_newton_iterations": [
        FieldInfoIni("max_nonlinear_iteration", int, "numerics"),
        FieldInfoAPI("max_non_linear_newton_iterations", int, 20),
        FieldInfoSqlite("max_nonlin_iterations", int,
                        "v2_numerical_settings"),
    ],
    "max_degree_gauss_seidel": [
        FieldInfoIni("maximum_degree", int, "numerics"),
        FieldInfoAPI("max_degree_gauss_seidel", int, 20),
        FieldInfoSqlite("max_degree", int,
                        "v2_numerical_settings"),
    ],
    "min_friction_velocity": [
        FieldInfoIni("minimum_friction_velocity", float, "numerics"),
        FieldInfoAPI("min_friction_velocity", float, 0.01),
        FieldInfoSqlite("minimum_friction_velocity", float,
                        "v2_numerical_settings"),
    ],
    "min_surface_area": [
        FieldInfoIni("minimum_surface_area", float, "numerics"),
        FieldInfoAPI("min_surface_area", float, 1.0e-8),
        FieldInfoSqlite("minimum_surface_area", float,
                        "v2_numerical_settings"),
    ],
    "use_preconditioner_cg": [
        FieldInfoIni("precon_cg", int, "numerics"),
        FieldInfoAPI("use_preconditioner_cg", int, 1),
        FieldInfoSqlite("precon_cg", int,
                        "v2_numerical_settings"),
    ],
    "preissmann_slot": [
        FieldInfoIni("preissmann_slot", float, "numerics"),
        FieldInfoAPI("preissmann_slot", float, 0.0),
        FieldInfoSqlite("preissmann_slot", float,
                        "v2_numerical_settings"),
    ],
    "pump_implicit_ratio": [
        FieldInfoIni("pump_implicit_ratio", float, "numerics"),
        FieldInfoAPI("pump_implicit_ratio", float, 1.0),
        FieldInfoSqlite("pump_implicit_ratio", float,
                        "v2_numerical_settings"),
    ],
    "limiter_slope_thin_water_layer": [
        FieldInfoIni("thin_water_layer_definition", float, "numerics"),
        FieldInfoAPI("limiter_slope_thin_water_layer", float, 0.01),
        FieldInfoSqlite("thin_water_layer_definition", float,
                        "v2_numerical_settings"),
    ],
    "use_of_cg": [
        FieldInfoIni("use_of_cg", int, "numerics"),
        FieldInfoAPI("use_of_cg", int, 20),
        FieldInfoSqlite("use_of_cg", int,
                        "v2_numerical_settings"),
    ],
    "use_nested_newton": [
        FieldInfoIni("nested_newton", int, "numerics"),
        FieldInfoAPI("use_nested_newton", bool, True),
        FieldInfoSqlite("use_of_nested_newton", int,
                        "v2_numerical_settings"),
    ],
    "flooding_threshold": [
        FieldInfoIni("flooding_threshold", float, "numerics"),
        FieldInfoAPI("flooding_threshold", float, 0.000001),
        FieldInfoSqlite("flooding_threshold", float,
                        "v2_global_settings"),
    ],
}

aggregation_settings_map = {
    "flow_variable": [
        AggregationFieldInfoOld("flow_variable", str),
        FieldInfoAPI("flow_variable", str, None),
        FieldInfoSqlite("flow_variable", str,
                        "v2_aggregation_settings"),
    ],
    "method": [
        AggregationFieldInfoOld("aggregation_method", str),
        FieldInfoAPI("method", str, None),
        FieldInfoSqlite("aggregation_method", str,
                        "v2_aggregation_settings"),
    ],
    "interval": [
        AggregationFieldInfoOld("timestep", float),
        FieldInfoAPI("interval", float, None),
        FieldInfoSqlite("timestep", str,
                        "v2_aggregation_settings"),
    ],
}


settings_map = {
    **general_settings_map,
    **time_step_settings_map,
    **numerical_settings_map,
}


swagger_definitions_map = {
    "GeneralSettings": general_settings_map,
    "NumericalSettings": numerical_settings_map,
    "TimeStepSettings": time_step_settings_map
}
