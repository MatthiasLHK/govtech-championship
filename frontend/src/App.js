import './App.css';
import TextBox from "./components/TextBox";
import 'bootstrap/dist/css/bootstrap.min.css';
import RankingTableA from "./components/RankingTableA";
import RankingTableB from "./components/RankingTableB";
import ClearButton from './components/ClearButton';
import RefreshButton from './components/RefreshButton';

function App() {
  return (
    <div className="App">
      <TextBox title="Team formation input" api="/team-creation" header="Team Sign Here!" placeholder="Please input teams registration here!"/>
      <TextBox title="Match results input" api="/submit-results" header="Match Results Here!" placeholder="Please input match results here!"/>
      <div className="Button-group">
        <RefreshButton />
        <ClearButton />
      </div>
      <RankingTableA />
      <RankingTableB />
    </div>
  );
}

export default App;
