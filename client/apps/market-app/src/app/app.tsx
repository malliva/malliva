import React from 'react';
import styles from './app.module.scss';
import { Route, BrowserRouter, Switch, Redirect } from 'react-router-dom';

import { MarketAppLandingPage } from 'libs/market-app/landing-page/src/index';
import { MarketAppSignIn } from 'libs/market-app/sign-in/src/index';
import { MarketAppSignUps } from 'libs/market-app/sign-ups/src/index';

export function App() {
  return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route path="/sign-in">
            <MarketAppSignIn />
          </Route>
          <Route path="/sign-up">
            <MarketAppSignUps />
          </Route>
          <Route path="/index">
            <MarketAppLandingPage />
          </Route>
          <Redirect to="/sign-in" />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
