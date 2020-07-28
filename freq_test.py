import math
def generate_frequencies(text):
    frequency = dict()
    for t in text:
        if t in frequency.keys():
            value = frequency[t] 
            frequency[t] = value+1
        else:
            frequency[t] =1
    return frequency;

def match_frequencies(text):
    valid_data = "humidity 45.5 temperature 55.5"
    baseline_freq = generate_frequencies(valid_data)
    baseline_keys = baseline_freq.keys()
    incoming_freq = generate_frequencies(text)
    rms_values =[]
    for freq in incoming_freq:
        if freq in baseline_keys:
            base_freq_value = baseline_freq[freq]
            incoming_freq_value = incoming_freq[freq]
            rms_values.append(pow(base_freq_value-incoming_freq_value, 2))
        else:
            incoming_freq_value = incoming_freq[freq]
            rms_values.append(pow(incoming_freq_value,2))
    rms = math.sqrt(sum(rms_values)/len(rms_values))
    return rms

def match_garbage_frequencies(text):
    valid_data = "abcdefghijklmnopqrstuvwxyz01234567890.~`!@#$%^&*()_+"
    baseline_freq = generate_frequencies(valid_data)
    baseline_keys = baseline_freq.keys()
    incoming_freq = generate_frequencies(text)
    rms_values =[]
    for freq in incoming_freq:
        if freq in baseline_keys:
            base_freq_value = baseline_freq[freq]
            incoming_freq_value = incoming_freq[freq]
            rms_values.append(pow(base_freq_value-incoming_freq_value, 2))
        else:
            incoming_freq_value = incoming_freq[freq]
            rms_values.append(pow(incoming_freq_value,2))
    rms = math.sqrt(sum(rms_values)/len(rms_values))
    return rms


valid_data = "humidity 45.5 temperature 55.5"
a = generate_frequencies(valid_data)
for i in a:
    print (i, a[i])

rms = match_frequencies(valid_data)
print(rms)
assert(rms==0.0)

valid_data1 = "humidity temperature"
rms = match_frequencies(valid_data1)
print(rms)
assert(rms<1.0)

invalid_data1 = "2372-2398-2389-2388,08/24,055"
rms = match_frequencies(invalid_data1)
print(rms)
assert(rms>1.0)
