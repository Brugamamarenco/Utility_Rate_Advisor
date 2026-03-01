import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import { Calendar, momentLocalizer } from "react-big-calendar";
import "react-big-calendar/lib/css/react-big-calendar.css";
import moment from "moment";
import "./style.css";

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
    }, {
      title:"$5.42 (+3.45%)",
      start: new Date(2026, 1, 5, 16, 0),
      end: new Date(2026, 1, 5, 17, 0),
    },

    {
      title:"$5.42 (+3.45%)",
      start: new Date(2026, 1, 5, 16, 0),
      end: new Date(2026, 1, 5, 17, 0),
    },
    {
      title:"$20.43 (+0.12%)",
      start: new Date(2026, 1, 20, 16, 0),
      end: new Date(2026, 1, 20, 17, 0),
    }
  ]);

  return (
    <div style={{height: "100vh", padding: "50px", width:"100%",border:"1px solid black"}}>
      <h1>credit.</h1>
      <Calendar
        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
        style={{width:"90%", height: "90%" }}
        eventPropGetter={(event) => ({
          style: {borderRadius:"5px",backgroundColor: "black", color: "white",padding:"10px" },
        })}
      />
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);