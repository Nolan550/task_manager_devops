import { ClipboardList } from "lucide-react";
import TaskItem from "./TaskItem";

export default function TaskList({
  tasks,
  onToggle,
  onEdit,
  onDelete,
}) {
  if (tasks.length === 0) {
    return (
      <div className="empty-state">
        <ClipboardList size={38} />
        <h3>No tasks found</h3>
        <p>Create a task or change your search and filters.</p>
      </div>
    );
  }

  return (
    <div className="task-list">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          onToggle={onToggle}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}