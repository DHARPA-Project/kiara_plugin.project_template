# kiara modules for: {{ cookiecutter.project_name }}

This package contains a set of commonly used/useful modules, pipelines, types and metadata schemas for [*Kiara*](https://github.com/DHARPA-project/kiara).


## Description

TODO

## Package content

{% raw %}{%{% endraw %} for info_category, details in get_info_for_categories('metadata.value_type','metadata.module', 'metadata.pipeline','metadata.operation_type', limit_to_package='kiara_plugin.{{ cookiecutter.project_slug }}').items() {% raw %}%}
### {{ details['title'] }}
{% for item, desc in details['items'].items() %}- [{{ item }}][]: {{ desc }} 
{% endfor %}
{% endfor %}
{% endraw %}

## Links

 - Documentation: [https://dharpa.org/kiara_plugin.{{ cookiecutter.project_slug }}](https://dharpa.org/kiara_plugin.{{ cookiecutter.project_slug }})
 - Code: [https://github.com/DHARPA-Project/kiara_plugin.{{ cookiecutter.project_slug }}](https://github.com/DHARPA-Project/kiara_plugin.{{ cookiecutter.project_slug }})


