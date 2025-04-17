"""
High level: Create a todo list with create, delete, list functionalities that support prioritization

Requirements:
1. Add new items (with priority)
2. Delete existing items
3. List all current items
4. Indicate missing priorities (between min -> max)

Assumptions
Listing all current items should be done in order of priority (lowest -> highest)
Adding a item will should always come with a priority
You should never be deleting an item that doesn't exist
We should not have identical items added to the list

Analysis
Space complexity: O(# calls to add_item)
Time complexity:
    - add_item: O(1)
    - delete_item: O(1)
    - list_items: O(nlogn)
    - missing_properties: O(n)

Future Improvements
- Cleanup UI of this CLI, maybe make a clean website to reach greater audience
- Add some bonus functionality, Ex. give me the task of highest priority (minHeap)
- Add the ability to check off a task rather than deleting it
- Add some Unit tests, assertions
"""


class TodoList:
    def __init__(self) -> None:
        self.items = {}  # {item: priority}

    def add_item(self, item_name: str, priority: int) -> None:
        if item_name in self.items:
            print(f"Items must be unique, {item_name} is already added")
        self.items[item_name] = priority

    def delete_item(self, item_name: str) -> None:
        if item_name not in self.items:
            print(f"{item_name} not in list")
            return
        del self.items[item_name]

    def list_items(self) -> None:
        print("Here is your TODO list:")
        sorted_items_by_priority = [(priority, item) for priority, item in sorted(
            self.items.items())]
        for priority, item in sorted_items_by_priority:
            print(f"{priority}: {item}")

    def missing_priorities(self) -> None:
        min_priority = min(self.items.values())
        max_priority = max(self.items.values())
        missing = []
        used_priorities = set(self.items.values())
        for i in range(min_priority, max_priority + 1):
            if i not in used_priorities:
                missing.append(str(i))
        print("Missing priorities are", " ".join(missing))


# TESTING
tasks = TodoList()
tasks.add_item("brush teeth", 1)
tasks.add_item("shower", 5)
tasks.add_item("put on deodorant lol jk", 10)
tasks.list_items()
tasks.missing_priorities()
tasks.delete_item("put on deodorant lol jk")
tasks.delete_item("I do not exist")
tasks.list_items()
tasks.missing_priorities()
