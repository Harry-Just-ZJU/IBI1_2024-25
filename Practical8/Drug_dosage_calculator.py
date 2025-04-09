
# 1 Drug dosage calculator

def volume(weight, strength):
    '''
    Parameter:
    weight: a float parameter represent the weight.
    strength: a string parameter represent the strength of paracetamol.

    Calculate:
    the volume of the paracetamol according to the two parameters.

    Return:
    the volume calculated.
    '''
    if weight < 10 or weight > 100:
        return 'Weight is outwith the expected range.'
    if strength == '120 mg/5 ml':
        strength_ = 120 / 5
    elif strength == '250 mg/5 ml':
        strength_ = 250 / 5
    else:
        return 'Paracetamol strength does not match an expected concentration.'

    dosage_volume = weight * 15 / strength_
    return str(dosage_volume) + ' ml'

# example
example = volume(30, '250 mg/5 ml')
print(example)


weight = float(input('please write your weight(in kg): '))
strength = input('please write the strength of paracetamol(120 mg/5 ml or 250 mg/5 ml): ')

print(volume(weight, strength))