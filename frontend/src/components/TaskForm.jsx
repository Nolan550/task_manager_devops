import { useEffect, useState } from "react";
import { X, Plus, Save } from "lucide-react";

export default function TaskForm({ onSubmit, editingTask, onCancel }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [priority, setPriority] = useState("medium");
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    if (editingTask) {
      setTitle(editingTask.title);
      setDescription(editingTask.description || "");
      setPriority(editingTask.priority);
    } else {
      setTitle("");
      setDescription("");
      setPriority("medium");
    }
  }, [editingTask]);

  async function handleSubmit(event) {
    event.preventDefault();

    if (!title.trim()) return;

    setSubmitting(true);

    try {
      await onSubmit({
        title: title.trim(),
        description: description.trim(),
        priority,
        completed: editingTask?.completed ?? false,
      });

      if (!editingTask) {
        setTitle("");
        setDescription("");
        setPriority("medium");
      }
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <div className="form-heading">
        <div>
          <span className="eyebrow">
            {editingTask ? "UPDATE TASK" : "NEW TASK"}
          </span>
          <h2>{editingTask ? "Edit task" : "Create a task"}</h2>
        </div>

        {editingTask && (
          <button
            type="button"
            className="icon-button"
            onClick={onCancel}
            aria-label="Cancel editing"
          >
            <X size={18} />
          </button>
        )}
      </div>

      <label htmlFor="title">Task title</label>
      <input
        id="title"
        type="text"
        placeholder="What needs to be done?"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
        maxLength={100}
        required
      />

      <label htmlFor="description">Description</label>
      <textarea
        id="description"
        placeholder="Add some details..."
        value={description}
        onChange={(event) => setDescription(event.target.value)}
        rows={4}
      />

      <label htmlFor="priority">Priority</label>
      <select
        id="priority"
        value={priority}
        onChange={(event) => setPriority(event.target.value)}
      >
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>

      <button className="primary-button" type="submit" disabled={submitting}>
        {editingTask ? <Save size={17} /> : <Plus size={17} />}
        {submitting
          ? "Saving..."
          : editingTask
            ? "Save changes"
            : "Create task"}
      </button>
    </form>
  );
}