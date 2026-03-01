import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import { Calendar, momentLocalizer } from "react-big-calendar";
import "react-big-calendar/lib/css/react-big-calendar.css";
import moment from "moment";

const localizer = momentLocalizer(moment);

function App() {
  const [events, setEvents] = useState([
    {
      title: "Team Meeting",
      start: new Date(2026, 1, 28, 10, 0), // Feb 28, 10AM
      end: new Date(2026, 1, 28, 11, 0),
    },
    {
      title: "Project Deadline",
      start: new Date(2026, 1, 28, 14, 0),
      end: new Date(2026, 1, 28, 15, 0),
    },
  ]);

  return (
    <div style={{ height: "100vh", padding: "20px" }}>
      <h1>My Calendar</h1>
      <Calendar
        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
        style={{ height: "90%" }}
        eventPropGetter={(event) => ({
          style: { backgroundColor: "#4285F4", color: "white" },
        })}
      />
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);