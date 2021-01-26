import service
import unittest

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}
print(TASKS)

# def test_id_exists():
#     task_id = TASK_ID
#     result_task = get_task(task_id)
#     if not result_task:
#         raise KeyError("Task with this ID is not in tasks")
#     if result_task != TASK_TEXT:
#         raise ValueError("Wrong text in the task")
#
# def test_id_doesnt_exist():
#     task_id = 2
#     result_task = get_task(task_id)
#     if result_task:
#         raise KeyError("Task with this ID should not be in tasks")


class TestGetTask(unittest.TestCase):
    def test_id_exists(self):
        service.TASKS = TASKS
        task_id = TASK_ID
        result_task = service.get_task(task_id)
        self.assertEqual(result_task, TASK_TEXT)

    def test_id_doesnt_exist(self):
        service.TASKS = TASKS
        task_id = 1
        result_task = service.get_task(task_id)
        self.assertFalse(result_task)

if __name__ == '__main__':
    unittest.main()