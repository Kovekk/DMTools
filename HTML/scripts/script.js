function selectCampaign(campaign) {
    try {
        document.querySelector(".cSelected").classList.toggle("cSelected");
    } catch(err) {}
    campaign.classList.toggle("cSelected");
}

function selectPlayer(player) {
    console.log("hi")
    try {
        document.querySelector("#playerPage div.selected").classList.toggle("selected")
    } catch(err) {}
    player.classList.toggle("selected")
}

function selectNpc(npc) {
    console.log("hi")
    try {
        document.querySelector("#NPCs div.selected").classList.toggle("selected")
    } catch(err) {}
    npc.classList.toggle("selected")
}

campaignList = document.querySelectorAll("#home ul li");
for (let i = 0; i < campaignList.length; i++) {
    campaignList[i].addEventListener("click", function() {selectCampaign(campaignList[i])});
}

playerList = document.querySelectorAll("#playerPage div.cards div");
for (let i = 0; i < playerList.length; i++) {
    playerList[i].addEventListener("click", function() {selectPlayer(playerList[i])});
}

npcList = document.querySelectorAll("#NPCs div.cards div");
for (let i = 0; i < npcList.length; i++) {
    npcList[i].addEventListener("click", function() {selectNpc(npcList[i])});
}