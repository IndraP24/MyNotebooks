# MIS200 Assessment 1 Case Study

# %% [markdown]
# Q1. Write the code for these two equations.   Let $R = 10000, C = 1e - 6,  V_s = 10$
#
# ### $$T = RC $$
#
# ### $$V_c = V_s (1 - 10^{-\frac{t}{T}})$$
#
# The builder will enter t.


def equation_1(t: float, R=10000, C=1e-6, V_s=10) -> float:
    T = R * C
    V_c = V_s * (1 - 10**(-t / T))
    return T, V_c


t = int(input("Enter the value of t: "))
T, V_c = equation_1(t)
print("For the value of t =", t, "\nthe value of T is",
      T, "\nthe value of V_c is", V_c, "\n\n")


# %% [markdown]
# Q2. Write the code to implement the equation below (ignore the units).
# Let $G = 6.67 \times 10^{-11} m^3 kg^{-1} s^{-2}, r = 384e6 m $
# ### $$F_g = G. \frac{m_1 . m_2}{r^2} $$
# The user will enter m1 and m2.


def equation_2(m_1: float, m_2: float) -> float:
    G = 6.67e-11
    r = 384e6
    F_g = G * m_1 * m_2 / r**2
    return F_g


m_1, m_2 = float(input("Enter the value of m_1: ")), float(
    input("Enter the value of m_2: "))
print("For the value of m_1 =", m_1, "and the value of m_2 =",
      m_2, "\nthe value of F_g is", equation_2(m_1, m_2), "\n\n")


# %% [markdown]
# Q3. Code the equation:
#
# ### $$ (\frac{6^{(2+a)}}{4+b}) + (c+180) \times (\frac{b}{a}) \times \frac{6+\frac{2.8}{3}-3^{2.5}}{\frac{4}{3}\times\frac{7}{3\times24}} $$
#
# The builder will enter all the parameters.


def equation_3(a: float, b: float, c: float) -> float:
    term1 = 6**(2+a)/(4+b)
    term2 = (c+180)*(b/a)*((6+(2.8/3)-3**2.5)/(4/3)*(7/(3*24)))
    return term1 + term2


a, b, c = float(input("Enter the value of a: ")), float(
    input("Enter the value of b: ")), float(input("Enter the value of c: "))

print("For the value of a =", a, ", b =", b, "and c =", c,
      "\nthe value of equation_3 is", equation_3(a, b, c), "\n\n")


# %% [markdown]
# Q4. Programs to covert the following units (the builder will enter the first unit in each case):
# - centimetre to millimetre
# - feet to meter
# - kilometres to meter
# - pound to kilogram
# - yard to inch


def convert(n: float, type: int) -> float:
    """_summary_
    Converts the input number to the desired type.
    type = 1: centimetre to millimetre
    type = 2: feet to meter
    type = 3: kilometres to meter
    type = 4: pound to kilogram
    type = 5: yard to inch

    Args:
        n (float): Number to convert
        type (int): Type of conversion desired as per given values

    Returns:
        float: Number converted to the desired type
    """
    if type == 1:
        return n * 10
    elif type == 2:
        return n * 0.3048
    elif type == 3:
        return n * 1000
    elif type == 4:
        return n * 0.453592
    elif type == 5:
        return n * 36
    else:
        return "Invalid type"


print("Refer the following table for the conversion of the number to the desired type:"
      "\n1. Centimetre to millimetre"
      "\n2. Feet to meter"
      "\n3. Kilometres to meter"
      "\n4. Pound to kilogram"
      "\n5. Yard to inch")
n, type = float(input("Enter the value of n: ")), int(
    input("Enter the value of type: "))
print("For the value of n =", n, "and type =", type,
      " conversion\nthe value of the converted number is", convert(n, type))
