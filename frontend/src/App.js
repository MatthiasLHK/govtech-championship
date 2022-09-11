import './App.css';
import TextBox from "./components/TextBox"

function App() {
  return (
    <div className="App">
      <div>
        <TextBox title="Team formation input" api="/team-creation"/>
        <TextBox title="Match results input" api="/submit-results"/>
      </div>
    </div>
  );
}

export default App;
