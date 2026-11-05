import { useEffect, useMemo, useState } from "react";
import {
  CheckCircle2,
  Circle,
  ClipboardList,
  ListTodo,
  Search,
  RefreshCw,
} from "lucide-react";

import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";
import { taskService } from "./services/taskService";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [editingTask, setEditingTask] = useState(null);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("all");

  async function loadTasks() {
    setLoading(true);
    setError("");

    try {
      const data = await taskService.getAll();
      setTasks(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadTasks();
  }, []);

  async function handleCreateOrUpdate(taskData) {
    try {
      if (editingTask) {
        await taskService.update(editingTask.id, taskData);
        setEditingTask(null);
      } else {
        await taskService.create(taskData);
      }

      await loadTasks();
    } catch (err) {
      setError(err.message);
      throw err;
    }
  }

  async function handleToggle(task) {
    try {
      await taskService.patch(task.id, {
        completed: !task.completed,
      });
      await loadTasks();
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleDelete(id) {
    if (!window.confirm("Are you sure you want to delete this task?")) {
      return;
    }

    try {
      await taskService.delete(id);

      if (editingTask?.id === id) {
        setEditingTask(null);
      }

      await loadTasks();
    } catch (err) {
      setError(err.message);
    }
  }

  const stats = useMemo(() => {
    const completed = tasks.filter((task) => task.completed).length;
    const pending = tasks.length - completed;

    return {
      total: tasks.length,
      completed,
      pending,
    };
  }, [tasks]);

  const filteredTasks = useMemo(() => {
    return tasks.filter((task) => {
      const matchesSearch =
        task.title.toLowerCase().includes(search.toLowerCase()) ||
        (task.description || "").toLowerCase().includes(search.toLowerCase());

      const matchesFilter =
        filter === "all" ||
        (filter === "pending" && !task.completed) ||
        (filter === "completed" && task.completed);

      return matchesSearch && matchesFilter;
    });
  }, [tasks, search, filter]);

  return (
    <main className="app-container">
      <header className="topbar">
        <div className="brand">
          <div className="brand-icon">
            <ListTodo size={23} />
          </div>
          <span>Task<span className="brand-highlight">Flow</span></span>
        </div>

        <span className="connection-status">
          <span className="status-dot" />
          Task Manager
        </span>
      </header>

      <section className="welcome-section">
        <div>
          <span className="eyebrow">YOUR WORKSPACE</span>
          <h1>Manage your tasks.</h1>
          <p>Stay organized, focused, and in control of your work.</p>
        </div>

        <button className="refresh-button" onClick={loadTasks}>
          <RefreshCw size={16} />
          Refresh
        </button>
      </section>

      {error && (
        <div className="error-banner">
          <span>{error}</span>
          <button onClick={() => setError("")}>Dismiss</button>
        </div>
      )}

      <section className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon blue"><ClipboardList /></div>
          <span>Total tasks</span>
          <strong>{stats.total}</strong>
        </div>

        <div className="stat-card">
          <div className="stat-icon orange"><Circle /></div>
          <span>Pending</span>
          <strong>{stats.pending}</strong>
        </div>

        <div className="stat-card">
          <div className="stat-icon green"><CheckCircle2 /></div>
          <span>Completed</span>
          <strong>{stats.completed}</strong>
        </div>
      </section>

      <section className="workspace">
        <div className="tasks-panel">
          <div className="section-heading">
            <div>
              <span className="eyebrow">OVERVIEW</span>
              <h2>Your tasks</h2>
            </div>
            <span className="task-count">{filteredTasks.length} tasks</span>
          </div>

          <div className="toolbar">
            <div className="search-box">
              <Search size={17} />
              <input
                type="search"
                placeholder="Search tasks..."
                value={search}
                onChange={(event) => setSearch(event.target.value)}
              />
            </div>

            <select
              className="filter-select"
              value={filter}
              onChange={(event) => setFilter(event.target.value)}
              aria-label="Filter tasks"
            >
              <option value="all">All tasks</option>
              <option value="pending">Pending</option>
              <option value="completed">Completed</option>
            </select>
          </div>

          {loading ? (
            <div className="loading-state">
              <div className="spinner" />
              Loading tasks from the server...
            </div>
          ) : (
            <TaskList
              tasks={filteredTasks}
              onToggle={handleToggle}
              onEdit={setEditingTask}
              onDelete={handleDelete}
            />
          )}
        </div>

        <aside className="form-panel">
          <TaskForm
            onSubmit={handleCreateOrUpdate}
            editingTask={editingTask}
            onCancel={() => setEditingTask(null)}
          />
        </aside>
      </section>

      <footer className="footer">
        <span>TaskFlow · Task Manager</span>
        <span>Powered by React and FastAPI</span>
      </footer>
    </main>
  );
}

export default App;