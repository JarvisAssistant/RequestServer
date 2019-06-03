import class_actions

CLASS_KEY = 'class'
CLASS_TEMPLATE = 'template'
CLASS_OBJ = 'object'
CLASS_ATTR = 'attribute'
CLASS_ATTR_TEMPLATE = 'attribute_template'

ATTR_TYPE_TOGGLE = 0
ATTR_TYPE_RANGE = 1

NAME_KEY = 'name'
ATTR_TYPE_KEY = 'type'
TOGGLE_KEY = 'toggle'
MIN_KEY = 'min'
MAX_KEY = 'max'
CURRENT_KEY = 'current'
ATTRIBUTES_KEY = 'attributes'

ACTION_TOGGLE = "toggle"
ACTION_ON = "on"
ACTION_OFF = "off"
ACTION_SET = "set"
ACTION_INCREASE_PER = "increase_per"
ACTION_DECREASE_PER = "decrease_per"
ACTION_INCREASE_FIX = "increase_fix"
ACTION_DECREASE_FIX = "decrease_fix"

CLASS_TEMPLATE_TEMPLATE = {
	CLASS_KEY : CLASS_TEMPLATE,
	NAME_KEY : None,
	ATTRIBUTES_KEY : []
}

CLASS_ATTR_TEMPLATE_TOGGLE_TEMPLATE = {
	CLASS_KEY : CLASS_ATTR_TEMPLATE,
	NAME_KEY : None,
	ATTR_TYPE_KEY : ATTR_TYPE_TOGGLE
}

CLASS_ATTR_TEMPLATE_RANGE_TEMPLATE = {
	CLASS_KEY : CLASS_ATTR_TEMPLATE,
	NAME_KEY : None,
	ATTR_TYPE_KEY : ATTR_TYPE_RANGE,
	MIN_KEY : 0,
	MAX_KEY : 0
}

CLASS_OBJ_TEMPLATE = {
	CLASS_KEY : CLASS_OBJ,
	NAME_KEY : None,
	ATTRIBUTES_KEY : []
}

CLASS_ATTR_TOGGLE_TEMPLATE = {
	CLASS_KEY : CLASS_ATTR,
	ATTR_TYPE_KEY : ATTR_TYPE_TOGGLE,
	TOGGLE_KEY : False
}

CLASS_ATTR_RANGE_TEMPLATE = {
	CLASS_KEY : CLASS_ATTR,
	ATTR_TYPE_KEY : ATTR_TYPE_RANGE,
	MIN_KEY : 0,
	MAX_KEY : 0,
	CURRENT_KEY : 0
}

class Attribute:
	@staticmethod
	def create_toggle_template(name):
		toggle_template = CLASS_ATTR_TEMPLATE_TOGGLE_TEMPLATE.copy()
		toggle_template[NAME_KEY] = name

		return toggle_template

	@staticmethod
	def create_range_template(name, min, max):
		range_template = CLASS_ATTR_TEMPLATE_RANGE_TEMPLATE.copy()
		range_template[NAME_KEY] = name
		range_template[MIN_KEY] = min
		range_template[MAX_KEY] = max

		return range_template

	@staticmethod
	def create_toggle(value=False):
		toggle = CLASS_ATTR_TOGGLE_TEMPLATE.copy()
		toggle[TOGGLE_KEY] = value

		return toggle

	@staticmethod
	def create_range(min=0, max=0, current=0):
		_range = CLASS_ATTR_RANGE_TEMPLATE.copy()
		_range[MIN_KEY] = min
		_range[MAX_KEY] = max
		_range[CURRENT_KEY] = current

		return _range

class Class:
	@staticmethod
	def create(name=''):
		clazz = CLASS_TEMPLATE_TEMPLATE.copy()
		clazz[NAME_KEY] = name

		return clazz

	@staticmethod
	def add_toggle_attribute(clazz, name):
		clazz[ATTRIBUTES_KEY].append(Attribute.create_toggle_template(name))

	@staticmethod
	def add_range_attribute(clazz, name, min, max):
		clazz[ATTRIBUTES_KEY].append(Attribute.create_range_template(name, min, max))

class Object:
	@staticmethod
	def create(clazz=Class.create()):
		obj = CLASS_OBJ_TEMPLATE.copy()

		obj[NAME_KEY] = clazz[NAME_KEY]
		obj[ATTRIBUTES_KEY] = Object.realize_attributes(clazz[ATTRIBUTES_KEY])

		return obj

	@staticmethod
	def set(obj, attr, key, value):
		obj[ATTRIBUTES_KEY][attr][key] = value

	@staticmethod
	def get(obj, attr, key):
		return obj[ATTRIBUTES_KEY][attr][key]

	@staticmethod
	def attr_type(obj, attr, type):
		return obj[ATTRIBUTES_KEY][attr][ATTR_TYPE_KEY] == type

	@staticmethod
	def toggle(obj, attr):
		if Object.attr_type(obj, attr, ATTR_TYPE_RANGE):
			value = Object.get(obj, attr, CURRENT_KEY)
			if value:
				Object.off(obj, attr)
			else:
				Object.on(obj, attr)
		else:
			value = Object.get(obj, attr, TOGGLE_KEY)
			Object.set(obj, attr, TOGGLE_KEY, not value)

	@staticmethod
	def on(obj, attr):
		if Object.attr_type(obj, attr, ATTR_TYPE_RANGE):
			Object.set(obj, attr, CURRENT_KEY, Object.get(obj, attr, MAX_KEY))
		else:
			Object.set(obj, attr, TOGGLE_KEY, True)

	@staticmethod
	def off(obj, attr):
		if Object.attr_type(obj, attr, ATTR_TYPE_RANGE):
			Object.set(obj, attr, CURRENT_KEY, Object.get(obj, attr, MIN_KEY))
		else:
			Object.set(obj, attr, TOGGLE_KEY, False)

	@staticmethod
	def get_toggle(obj, attr):
		return Object.get(obj, attr, TOGGLE_KEY)

	@staticmethod
	def get_range_min(obj, attr):
		return Object.get(obj, attr, MIN_KEY)

	@staticmethod
	def get_range_max(obj, attr):
		return Object.get(obj, attr, MAX_KEY)

	@staticmethod
	def get_range_current(obj, attr):
		return Object.get(obj, attr, CURRENT_KEY)

	@staticmethod
	def set_toggle(obj, attr, value):
		Object.set(obj, attr, TOGGLE_KEY, value)

	@staticmethod
	def set_range_current(obj, attr, value):
		_min = Object.get(obj, attr, MIN_KEY)
		_max = Object.get(obj, attr, MAX_KEY)
		Object.set(obj, attr, CURRENT_KEY, max(_min, min(_max, value)))

	@staticmethod
	def realize_attributes(attributes):
		realization = {}

		for attr in attributes:
			real = None
			if attr[ATTR_TYPE_KEY] == ATTR_TYPE_RANGE:
				real = Attribute.create_range(min=attr[MIN_KEY], max=attr[MAX_KEY])
			else:
				real = Attribute.create_toggle()

			realization[attr[NAME_KEY]] = real


		return realization





