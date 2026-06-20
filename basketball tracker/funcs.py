def percentage(made, attempts):
    if attempts == 0:
        return 0
    else:
        return (made/attempts) *100

def total_shots(sessions):
    total_attempts = 0
    total_made = 0

    for session in sessions:
        total_attempts += session["attempts"]
        total_made += session["made"] 

    return total_made,total_attempts

def average(sessions, made, attempts):
    made, attempts = total_shots(sessions)

    return percentage(made, attempts)

def best_practice(sessions):
    best_session = sessions[0]

    for session in sessions:
        if percentage(session["made"], session["attempts"])\
            > percentage(best_session["made"], best_session["attempts"]):
            best_session = session
