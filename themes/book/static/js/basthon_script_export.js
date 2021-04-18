function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
}

function formatCopyText(textContent,
  copybuttonPromptText,
  isRegexp = false,
  onlyCopyPromptLines = true,
  removePrompts = true) {

  var regexp;
  var match;

  // create regexp to capture prompt and remaining line
  if (isRegexp) {
    regexp = new RegExp('^(' + copybuttonPromptText + ')(.*)')
  } else {
    regexp = new RegExp('^(' + escapeRegExp(copybuttonPromptText) + ')(.*)')
  }

  const outputLines = [];
  var promptFound = false;
  for (const line of textContent.split('\n')) {
    match = line.match(regexp)
    if (match) {
      promptFound = true
      if (removePrompts) {
        outputLines.push(match[2])
      } else {
        outputLines.push(line)
      }
    } else {
      if (!onlyCopyPromptLines) {
        outputLines.push(line)
      }
    }
  }

  // If no lines with the prompt were found then just use original lines
  if (promptFound) {
    textContent = outputLines.join('\n');
  }

  // Remove a trailing newline to avoid auto-running when pasting
  if (textContent.endsWith("\n")) {
    textContent = textContent.slice(0, -1)
  }
  return textContent
}

function codeToUrl(textcode) {

  // to retain the Line breaks.
  textcode = textcode.replace(/\r\n|\r|\n/g, "\r\n");
  // const url = new URL(window.location.href);
  const url = new URL("https://console.basthon.fr/");
  url.hash = "";
  url.searchParams.delete("from"); // take care of collapsing params
  let script;
  try {
    script = Base64.fromUint8Array(pako.deflate(textcode), true);
  } catch { // fallback
    script = encodeURIComponent(textcode).replace(/\(/g, '%28').replace(/\)/g, '%29');
  }
  url.searchParams.set('script', script);
  return url;
};


function createCopyButton(highlightDiv) {
  if (highlightDiv.querySelectorAll(".language-python").length > 0) {
    const button = document.createElement("button");
    button.className = "copy-code-button";
    button.type = "button";
    button.innerText = "Python";
    button.addEventListener("click", () =>
      copyCodeToClipboard(button, highlightDiv)
    );
    addCopyButtonToDom(button, highlightDiv);

  }
}

async function copyCodeToClipboard(button, highlightDiv) {
  var codeToCopy = highlightDiv.querySelector(".highlight > pre > code")
    .innerText;
  try {
    var codeToCopy = formatCopyText(codeToCopy, ">>> ")
  } catch (_) {

  }
  try {
    result = await navigator.permissions.query({name: "clipboard-write"});
    if (result.state == "granted" || result.state == "prompt") {
      await navigator.clipboard.writeText(codeToCopy);
    } else {
      copyCodeBlockExecCommand(codeToCopy, highlightDiv);
    }
  } catch (_) {
    copyCodeBlockExecCommand(codeToCopy, highlightDiv);
  } finally {
    codeWasCopied(button);
  }
  let basthon_url = codeToUrl(codeToCopy);
  console.log(basthon_url);
  console.log(basthon_url.href);
  window.open(basthon_url);
}

function copyCodeBlockExecCommand(codeToCopy, highlightDiv) {
  const textArea = document.createElement("textArea");
  textArea.contentEditable = "true";
  textArea.readOnly = "false";
  textArea.className = "copyable-text-area";
  textArea.value = codeToCopy;
  highlightDiv.insertBefore(textArea, highlightDiv.firstChild);
  const range = document.createRange();
  range.selectNodeContents(textArea);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  textArea.setSelectionRange(0, 999999);
  document.execCommand("copy");
  highlightDiv.removeChild(textArea);
}

function codeWasCopied(button) {
  button.blur();
  button.innerText = "Opening...";
  setTimeout(function () {
    button.innerText = "Python";
  }, 2000);
}

function addCopyButtonToDom(button, highlightDiv) {
  highlightDiv.insertBefore(button, highlightDiv.firstChild);
  const wrapper = document.createElement("div");
  wrapper.className = "highlight-wrapper";
  highlightDiv.parentNode.insertBefore(wrapper, highlightDiv);
  wrapper.appendChild(highlightDiv);
}

document
  .querySelectorAll(".highlight")
  .forEach((highlightDiv) => createCopyButton(highlightDiv));
