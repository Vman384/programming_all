import React, { useState } from 'react';

function App() {
  const [number, setNumber] = useState(Math.floor(Math.random() * 100) + 1);

  const generateNumber = () => {
    setNumber(Math.floor(Math.random() * 100) + 1);
  };

  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        backgroundColor: '#fff',
        flexDirection: 'column',
      }}
    >
      <h1>{number}</h1>
      <button onClick={generateNumber}>Generate New Number</button>
    </div>
  );
}

export default App;
