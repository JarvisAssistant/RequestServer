import datetime
import class_actions
import classification as c

def get_time():
	dt = datetime.datetime.now()

	return {
		"year" : dt.year,
		"month" : dt.month,
		"day" : dt.day,
		"hour" : dt.hour,
		"minute" : dt.minute,
		"second" : dt.second
	}


custom_class = {
}
	
custom_object = {
}

custom_class['light'] = c.Class.create('light')
c.Class.add_toggle_attribute(custom_class['light'], 'default')
c.Class.add_range_attribute(custom_class['light'], 'brightness', 1, 100)

custom_object['my_light'] = c.Object.create(custom_class['light'])


def custom_object_action(obj, attribute, action, value):
	return _custom_object_action(obj, attribute, action, value)

def _custom_object_action(obj, attribute, action, value):
	assert(
		action == c.ACTION_TOGGLE or
		action == c.ACTION_ON or
		action == c.ACTION_OFF or
		action == c.ACTION_SET)

	new = custom_object[obj].copy()

	# Get associated action
	action_name = "action_%s_%s" % (new[c.NAME_KEY], attribute)

	# If the action doesn't exist, we can't execute
	if not hasattr(class_actions, action_name):
		return { "error" : "No custom action defined" }

	# Find the custom object
	new = custom_object[obj].copy()

	# Do the action
	if not value:
		if action == c.ACTION_TOGGLE:
			c.Object.toggle(new, attribute)
		elif action == c.ACTION_ON:
			c.Object.on(new, attribute)
		else:
			c.Object.off(new, attribute)
	else:
		assert(action == c.ACTION_SET)
		c.Object.set_range_current(new, attribute, value)

	# Get the function
	func = getattr(class_actions, action_name)

	# Run the function to completion with new object state
	result = func(new)

	# If everything went well, result should be None
	if result:
		return { "error" : result }

	# replace old object state if successful
	custom_object[obj] = new

	return {}








