import './App.css';
import TextBox from "./components/TextBox"

function App() {
  return (
    <div className="App">
      <div>
        <TextBox title="Team formation input" api="/team-creation" value=""/>
        <TextBox title="Match results input" api="/submit-results" value="teamA teamB 0 1"/>
      </div>
    </div>
  );
}

export default App;
