from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
# Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

# Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    pass

def test_middle_school_student_summary_with_transportation():
    pass

def test_middle_school_student_summary_without_transportation():
    pass

# Test summary when there are no classes passed
def test_middle_school_student_without_classes():
    # Arrange
    name = "Larry"
    grade = "7"
    classes = []

    # Act
    larry = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    # Assert
    assert len(larry.classes) == 0

# Test summary if gets_transportation parameter is not passed in at all
def test_middle_school_student_no_transportation_paramter_passed():
    # Arrange
    name = "Mozart"
    grade = "6"
    classes = ["Classical Music", "Music Theory", "Composition"]

    # Act
    mozart = MiddleSchoolStudent(name, grade, classes)

    # Assert
    assert mozart.gets_transportation == False