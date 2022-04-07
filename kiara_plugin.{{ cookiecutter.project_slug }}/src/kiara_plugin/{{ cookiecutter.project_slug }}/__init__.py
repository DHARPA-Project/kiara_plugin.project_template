# -*- coding: utf-8 -*-

"""Top-level package for kiara_plugin.{{ cookiecutter.project_slug }}."""


import structlog
import os

from kiara.utils.class_loading import (
    KiaraEntryPointItem,
    find_kiara_modules_under,
    find_data_types_under,
    find_pipeline_base_path_for_module,
    find_value_metadata_models_under,
)

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"



KIARA_METADATA = {
    "authors": [
        {"name": __author__, "email": __email__}
    ],
    "description": "Kiara modules for: {{ cookiecutter.project_name }}",
    "references": {
        "source_repo": {
            "desc": "The module package git repository.",
            "url": "https://github.com/DHARPA-Project/kiara_plugin.{{ cookiecutter.project_slug }}",
        },
        "documentation": {
            "desc": "The url for the module package documentation.",
            "url": "https://dharpa.org/kiara_plugin.{{ cookiecutter.project_slug }}/",
        },
    },
    "tags": ["{{ cookiecutter.project_slug }}"],
    "labels": {
        "package": "kiara_plugin.{{ cookiecutter.project_slug }}"
    }
}

find_modules: KiaraEntryPointItem = (
    find_kiara_modules_under, "kiara_plugin.{{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}"
)
find_value_metadata: KiaraEntryPointItem = (
    find_value_metadata_models_under,
    "kiara_plugin.{{ cookiecutter.project_slug }}.models",
)
find_data_types: KiaraEntryPointItem = (
    find_data_types_under,
    "kiara_plugin.{{ cookiecutter.project_slug }}.data_types",
)
find_pipelines: KiaraEntryPointItem = (
    find_pipeline_base_path_for_module,
    "kiara_plugin.{{ cookiecutter.project_slug }}.pipelines",
)


def get_version():
    from pkg_resources import DistributionNotFound, get_distribution

    try:
        # Change here if project is renamed and does not equal the package name
        dist_name = __name__
        __version__ = get_distribution(dist_name).version
    except DistributionNotFound:

        try:
            version_file = os.path.join(os.path.dirname(__file__), "version.txt")

            if os.path.exists(version_file):
                with open(version_file, encoding="utf-8") as vf:
                    __version__ = vf.read()
            else:
                __version__ = "unknown"

        except (Exception):
            pass

        if __version__ is None:
            __version__ = "unknown"

    return __version__
