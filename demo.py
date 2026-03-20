import random

def check_location(gps, network):
    if gps == network:
        return True
    return False

def check_weather(api_weather, user_weather):
    return api_weather == user_weather

def behavior_analysis(speed):
    if speed > 120:
        return False
    return True

def calculate_risk(location_ok, weather_ok, behavior_ok):
    score = 0
    if not location_ok:
        score += 30
    if not weather_ok:
        score += 40
    if not behavior_ok:
        score += 20
    return score

def decision(score):
    if score < 30:
        return "✅ APPROVED"
    elif score < 60:
        return "⚠ FLAGGED"
    else:
        return "❌ REJECTED"

# ---- TEST CASES ----

print("---- Normal User ----")
loc = check_location("Coimbatore", "Coimbatore")
weather = check_weather("Rain", "Rain")
behavior = behavior_analysis(40)

score = calculate_risk(loc, weather, behavior)
print("Decision:", decision(score))


print("\n---- Fraud User ----")
loc = check_location("Chennai", "Coimbatore")
weather = check_weather("No Rain", "Rain")
behavior = behavior_analysis(200)

score = calculate_risk(loc, weather, behavior)
print("Decision:", decision(score))