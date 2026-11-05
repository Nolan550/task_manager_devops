import { Check, Pencil, Trash2 } from "lucide-react";

export default function TaskItem({ task, onToggle, onEdit, onDelete }) {
  return (
    <article className={`task-item ${task.completed ? "completed" : ""}`}>
      <button
        className={`check-button ${task.completed ? "checked" : ""}`}
        onClick={() => onToggle(task)}
        aria-label={task.completed ? "Mark as pending" : "Mark as completed"}
      >
        {task.completed && <Check size={15} />}
      </button>

      <div className="task-content">
        <h3>{task.title}</h3>
        {task.description && <p>{task.description}</p>}

        <div className="task-meta">
          <span className={`priority ${task.priority}`}>
            {task.priority} priority
          </span>
          <span className="task-status">
            {task.completed ? "Completed" : "Pending"}
          </span>
        </div>
      </div>

      <div className="task-actions">
        <button
          className="icon-button"
          onClick={() => onEdit(task)}
          aria-label="Edit task"
        >
          <Pencil size={17} />
        </button>

        <button
          className="icon-button delete-button"
          onClick={() => onDelete(task.id)}
          aria-label="Delete task"
        >
          <Trash2 size={17} />
        </button>
      </div>
    </article>
  );
}