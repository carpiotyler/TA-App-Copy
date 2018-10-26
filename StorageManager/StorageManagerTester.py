from StorageManager.AbstractStorageManager import Course, User, AbstractStorageManager

testCourse = ["CS", "351", ["401", "801"], "Data Structures and Algorithms", "Hard class"]

print(testCourse[Course.SECTIONS.value])
#Will return "351'
