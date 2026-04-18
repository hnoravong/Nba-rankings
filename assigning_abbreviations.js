PLAYERS = rawData.map(p => ({
    ...p,
    pts: p.points_per_game,
    reb: p.rebounds_per_game,
    ast: p.assists_per_game,
    stl: p.steals_per_game,
    blk: p.blocks_per_game,
    tov: p.turnovers_per_game,
    mpg: p.minutes_per_game,
    gp:  p.games_played,
    pos: p.position,
    name: p.player_name,
    
    fg_pct:  +(p.fg_pct  * 100).toFixed(1),
    fg3_pct: +(p.fg3_pct * 100).toFixed(1),
    ft_pct:  +(p.ft_pct  * 100).toFixed(1),
  }));