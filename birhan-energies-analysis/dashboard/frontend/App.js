import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine, ResponsiveContainer } from 'recharts';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/prices').then(res => setData(res.data));
    axios.get('http://localhost:5000/api/events').then(res => setEvents(res.data));
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Birhan Energies: Brent Oil Price Analysis</h2>
      <div style={{ width: '100%', height: 400 }}>
        <ResponsiveContainer>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Date" />
            <YAxis domain={['auto', 'auto']} />
            <Tooltip />
            <Line type="monotone" dataKey="Price" stroke="#8884d8" dot={false} />
            
            {/* Highlight Event Change Points */}
            {events.map((event, idx) => (
              <ReferenceLine key={idx} x={event.Date} stroke="red" label={{ position: 'top', value: event.Category, fill: 'red', fontSize: 10 }} />
            ))}
          </LineChart>
        </ResponsiveContainer>
      </div>
      <h3>Key Market Events</h3>
      <ul>
        {events.slice(-5).map((e, i) => <li key={i}><strong>{e.Date}</strong>: {e.Event}</li>)}
      </ul>
    </div>
  );
}

export default App;