# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line

# Part 1


def greet(name, greeting_template="Hello, <name>!"):
    return greeting_template.replace("<name>", name)


# Part 2


def force(mass, body="earth"):
    gravity_factor = {
        "mercury": 3.7,
        "venus": 8.9,
        "earth": 9.8,
        "moon": 1.6,
        "mars": 3.7,
        "jupiter": 23.1,
        "saturn": 9.0,
        "uranus": 8.7,
        "neptune": 11.0,
        "pluto": 0.7,
    }

    if body.lower() in gravity_factor:
        gravity = gravity_factor[body.lower()]
        force = mass * gravity
        return force
    else:
        print("Body not found.")


# Part 3


def pull(m1, m2, d):
    g = 6.674 * (10**-11)
    f = (g * m1 * m2) / d**2

    return f
