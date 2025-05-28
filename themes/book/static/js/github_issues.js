
  const url = `https://api.github.com/repos/${username}/${repository}/issues/${issueNumber}`;
  const proxyUrl = `https://corsproxy.io/?${encodeURIComponent(url)}`;

  fetch(proxyUrl)
    .then(response => {
      if (!response.ok) throw new Error("Issue non trouvée ou accès refusé");
      return response.json();
    })
    .then(data => {
      const htmlContent = `
        <h1>${data.title}</h1>
        <div>${marked.parse(data.body || "_(Corps vide)_")}</div>
      `;
      document.getElementById("github-issue").innerHTML = htmlContent;
    })
    .catch(error => {
      document.getElementById("github-issue").innerText = "Erreur de chargement : " + error.message;
      console.error(error);
    });
