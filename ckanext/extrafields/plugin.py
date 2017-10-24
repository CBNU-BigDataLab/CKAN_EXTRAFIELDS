import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ExtrafieldsPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)

    # IConfigurer
    # TODO: TO MODIFY THE INTERFACE FORM

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'extrafields')

    # TODO: TO MODIFY THE DATASET FORM
    def _modify_package_schema(self, schema):
        schema.update({
            'language': [toolkit.get_validator('ignore_missing'),
			 toolkit.get_converter('convert_to_extras')]
        })
        return schema
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'extrafields')

    def create_package_schema(self):
        # TODO: TO GRAP THE DEFAULT SCHEMA IN OUR PLUGIN
        schema = super(ExtrafieldsPlugin, self).create_package_schema()
        # TODO: OUR CUSTOM FIELDS
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        #TODO: TO GRAP THE DEFAULT SCHEMA IN OUR PLUGIN
        schema = super(ExtrafieldsPlugin, self).update_package_schema()
        #TODO: OUR CUSTOM FIELDS
        schema = self._modify_package_schema(schema)
        return schema

    def schow_package_schema(self):
        schema = super(ExtrafieldsPlugin, self).show_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
    def is_fallback(self):
        return True
    def package_types(self):
	return []
