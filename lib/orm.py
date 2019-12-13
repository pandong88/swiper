

class ModelMixin():
    def to_dict(self, ignore_fields=()):

        attr_dict = {}
        for field in self._meta.fields:
            name = field.attname
            if name not in ignore_fields:
                attr_dict[name] = getattr(self, name=name)

        return attr_dict

