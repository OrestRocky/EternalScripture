const contractAddress = "0xD7ACd2a9FD159E69Bb102A1ca21C9a3e3A5F771B"; //.
let abi;

fetch("../ProphecyArchiveABI.json")
  .then(res => res.json())
  .then(json => {
    abi = json;
  });

async function fetchCID() {
  const docId = document.getElementById("docId").value;

  if (!window.ethereum) {
    alert("Встановіть MetaMask!");
    return;
  }

  await ethereum.request({ method: 'eth_requestAccounts' });
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const signer = provider.getSigner();
  const contract = new ethers.Contract(contractAddress, abi, signer);

  try {
    const cid = await contract.getCID(docId);
    const url = `https://ipfs.io/ipfs/${cid}`;
    window.open(url, "_blank");
  } catch (err) {
    console.error("Помилка:", err);
    alert("0xD7ACd2a9FD159E69Bb102A1ca21C9a3e3A5F771B");
  }
}
