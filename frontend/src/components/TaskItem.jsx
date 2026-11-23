
import { Check, Pencil, Trash2, CalendarDays } from "lucide-react";

function formatDueDate(dateString) {
  if (!dateString) return null;

  const [year, month, day] = dateString.split("-").map(Number);

  const date = new Date(year, month - 1, day);

  return date.toLocaleDateString(undefined, {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

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

        {task.due_date && (
          <div className="due-date">
            <CalendarDays size={15} />
            <span>Due: {formatDueDate(task.due_date)}</span>
          </div>
        )}

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
