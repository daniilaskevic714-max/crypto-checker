import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  const disposable = vscode.commands.registerCommand('cryptoChecker.showPrices', () => {
    vscode.window.showInformationMessage('Crypto Checker is active!');
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}