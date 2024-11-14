def function_call(message):
    return message

# Good: alternating quotes
print(f"Text with function call {function_call('string with single quotes')} here.")
print(f'Text with function call {function_call("string with double quotes")} here.')

# Bad: non-alternating quotes
print(f"Text with function call {function_call("string with double quotes")} here.")  # Bad
print(f'Text with function call {function_call('string with single quotes')} here.')  # Bad

# Good: alternating quotes and escaped double quotes
print(f"Text with function call {function_call('string with single quotes and \"escaped double quotes\"')} here.")
print(f'Text with function call {function_call("string with double quotes and \"escaped double quotes\"")} here.')

# Good: alternating quotes and escaped single quotes
print(f"Text with function call {function_call('string with single quotes and \'escaped double quotes\'')} here.")
print(f'Text with function call {function_call("string with double quotes and \'escaped double quotes\'")} here.')

# Bad: Trailing whitespace   
print(f"Trailing whitespace on this and following line")    
    
# Bad: Trailing tab   
print(f"Trailing tab on this and following line")	
	

print("Expected bad non-alternating lines are [9, 10] only.")
print("Expected bad trailing whitespace lines are [20 - 25] only.")
