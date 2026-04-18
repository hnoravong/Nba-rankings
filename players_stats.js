let PLAYERS = [];

async function loadPlayers() {
  const res = await fetch('players_clean.json');
  PLAYERS = await res.json();
}

loadPlayers().then(() => {
  console.log(`Loaded ${PLAYERS.length} players`);
});