import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, ReferenceLine, ResponsiveContainer } from 'recharts';

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/prices').then(res => setPrices(res.data));
    axios.get('http://127.0.0.1:5000/api/events').then(res => setEvents(res.data));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Birhan Energies Dashboard</h1>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={prices}>
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="Price" stroke="#2563eb" dot={false} />
          {events.map((ev, i) => (
            <ReferenceLine key={i} x={ev.Date} stroke="red" label={ev.Category} />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;