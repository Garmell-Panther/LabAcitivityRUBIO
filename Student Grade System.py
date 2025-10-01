import re

def student_grading_system():
    grades = []
    print("📘 Student Grading System")
    print("Enter grades between 0 and 100. Type -1 to stop.")
    print("You can enter multiple grades separated by space or comma (e.g. 90 85 88).\n")

    while True:
        s = input("Enter grade(s) (-1 to stop): ").strip()
        if s == "":
            print("❌ Empty input. Please enter a number or -1.")
            continue

        # Split on commas or whitespace so user may enter "90 85" or "90,85"
        tokens = re.split(r'[,\s]+', s)
        stop = False

        for tok in tokens:
            if tok == "":
                continue
            try:
                value = float(tok)
            except ValueError:
                print(f"❌ '{tok}' is not a number. Ignored.")
                continue

            # sentinel
            if value == -1:
                stop = True
                break

            # valid grade?
            if 0 <= value <= 100:
                grades.append(value)
                # optionally: print confirmation
                # print(f"✔️ Recorded {value}")
            else:
                print(f"❌ {value} is outside 0–100. Ignored.")

        if stop:
            break

    if not grades:
        print("\n⚠️ No valid grades entered.")
        return

    avg = sum(grades) / len(grades)
    point_grade = ((100 - avg) + 10) / 10

    # Remarks table (as per your spec)
    if avg < 50:
        remarks = "Dropped"
    elif avg < 75:
        remarks = "Failed"
    elif 75 <= avg <= 79:
        remarks = "Passed – Satisfactory"
    elif 80 <= avg <= 84:
        remarks = "Passed – Good"
    elif 85 <= avg <= 89:
        remarks = "Passed – Average"
    elif 90 <= avg <= 99:
        remarks = "Passed – Very Good"
    else:  # avg == 100
        remarks = "Passed – Excellent"

    # Nicely format the output
    formatted_grades = [f"{g:.2f}" for g in grades]
    print("\n📊 Results")
    print("Grades Entered:", formatted_grades)
    print(f"Average Grade: {avg:.2f}")
    print(f"Point Grade: {point_grade:.2f}")
    print("Remarks:", remarks)


# Run the program
if __name__ == "__main__":
    student_grading_system()
