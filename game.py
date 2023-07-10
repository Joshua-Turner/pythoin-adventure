class Game:
    def __init__(self, character, path, current_step_id=None):
        self.character = character
        self.path = path
        self.current_step_id = (
            current_step_id
            if isinstance(current_step_id, str)
            else self.get_first_step_id()
        )
        self.all_steps = self.build_ids_list()

    def build_ids_list(self):
        steps_list = []

        def collect_ids(_, __, step_id):
            steps_list.append(step_id)
            return True

        self.traverse(collect_ids)
        return steps_list

    def step_exists(self, step_id):
        try:
            self.all_steps.index(step_id)
        except ValueError:
            return False
        return True

    def get_first_step_id(self):
        return self.path["name"] + "." + self.path["action"][0]["name"]

    def is_path(self, path):
        return (
            True
            if isinstance(path, dict) and isinstance(path["action"], list)
            else False
        )

    def traverse(self, callback, path=None, base_step_id=None):
        path = path if self.is_path(path) else self.path
        step_id = base_step_id if isinstance(base_step_id, str) else path["name"]
        should_continue = True
        for step in path["action"]:
            current_step_id = step_id + "." + step["name"]
            is_path = self.is_path(step)
            if callback(step, is_path, current_step_id) == False:
                should_continue = False
                break

            if is_path and not self.traverse(callback, step, current_step_id):
                should_continue = False
                break

        return should_continue

    def find(self, step_id):
        if not self.step_exists(step_id):
            print('Step ID: "' + step_id + '" not found')
            return None

        step = None
        is_path = None

        def matches_pos(_step, _is_path, _step_id):
            if step_id == _step_id:
                nonlocal step
                step = _step
                nonlocal is_path
                is_path = _is_path
                return False

        self.traverse(matches_pos)

        return {"step": step, "is_path": is_path, "step_id": step_id}

    def play(self, from_path=None):
        new_step_id = from_path if isinstance(from_path, str) else self.current_step_id

        if not self.find(new_step_id):
            return

        self.current_step_id = new_step_id
        running = False

        def run_step(step, is_path, step_id):
            if step_id == self.current_step_id:
                nonlocal running
                running = True

            if not running:
                return

            if not is_path:
                result = step["action"](character=self.character, step_id=step_id)
                if result != True:
                    if isinstance(result, str):
                        self.play(result)
                    return False

        self.traverse(run_step)
