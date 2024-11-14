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

print("Expected bad lines are 9 and 10 only.")
