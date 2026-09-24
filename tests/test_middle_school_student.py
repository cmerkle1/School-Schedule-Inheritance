from school_schedule.middle_school_student import MiddleSchoolStudent

#constructor with transportation = true
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

#default transportation = False
def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    # Assert
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert ellis.gets_transportation == False

#summary includes transportation when True
def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(
        name,
        grade,
        classes,
        gets_transportation=True
    )

    # Assert
    assert ellis.summary() == "Ellis is a junior enrolled in 1 classes: Painting\nEllis has transportation"

#summary includes transportation status when False
def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(
        name,
        grade,
        classes,
        gets_transportation=False
    )

    # Assert
    assert ellis.summary() == "Ellis is a junior enrolled in 1 classes: Painting\nEllis doesn't have transportation"

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

#Test does child class still have the add_class method from parent class
def test_add_class():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    new_class = "Writing"

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)
    ellis.add_class(new_class)

    # Assert
    assert len(ellis.classes) == 2 