import React from 'react';
import styles from './app.module.scss';
import {
  Route,
  BrowserRouter,
  Switch,
  Redirect,
  useRouteMatch,
} from 'react-router-dom';
import { Provider } from 'react-redux';
import { Store } from '@reduxjs/toolkit';

import { MarketAppLandingPage } from 'libs/market-app/landing-page/src/index';
import { MarketAppSignIn } from 'libs/market-app/sign-in/src/index';
import { MarketAppSignUps } from 'libs/market-app/sign-ups/src/index';
import { MarketAppItemDetails } from 'libs/market-app/item-details/src/index';
import { SharedAuthGuard } from 'libs/shared/auth-guard/src/index';

export function App(props: { store: Store }) {
  return (
    <Provider store={props.store}>
      <BrowserRouter>
        <Switch>
          <Route path="/sign-in">
            <MarketAppSignIn />
          </Route>
          {/* Dashboard should be here */}
          <SharedAuthGuard
            path="/protected"
            component={MarketAppItemDetails}
            auth={false}
          />
          <Route path="/sign-up">
            <MarketAppSignUps />
          </Route>
          <Route path="/item-id">
            <MarketAppItemDetails />
          </Route>
          <Route path="/">
            <MarketAppLandingPage />
          </Route>
          {/* <Redirect to="/sign-in" /> */}
        </Switch>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
