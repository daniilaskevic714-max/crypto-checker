import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
 const disposable = vscode.commands.registerCommand('cryptoChecker.showPrices', async () => {
  try {
   const api='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd';
   const response = await fetch(api);
   const data = await response.json();
   vscode.window.showInformationMessage(`BTC: $${data.bitcoin.usd} | ETH: $${data.ethereum.usd}`);
  } catch {
   vscode.window.showErrorMessage('Failed to fetch crypto prices');
  }
 });
 context.subscriptions.push(disposable);
}

export function deactivate() {}