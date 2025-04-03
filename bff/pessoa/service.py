from .task import Task


class Service:
    def save(self, dto):
        task = Task()
        result = task.save(dto)
        return result

    def update(self, dto, id):
        task = Task()
        result = task.update(dto, id)
        return result

    def delete(self, id):
        task = Task()
        result = task.delete(id)
        return result

    def get(self, request):
        task = Task()
        result = task.get(request)
        return result

    def search(self, dto):
        task = Task()
        result = task.search(dto)
        return result

    def calculate_ideal_weight(self, dto):
        task = Task()
        result = task.calculate_ideal_weight(dto)
        return result
