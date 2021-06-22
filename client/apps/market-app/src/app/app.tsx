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
import { MarketAppDashboard } from 'libs/market-app/dashboard/src/index';
import { MarketAppTopMenu } from '@client/market-app/top-menu';

const menu = [
  { name: 'Home', link: '#', type: '' },
  { name: 'About', link: '#', type: '' },
  { name: 'Blog', link: '#', type: '' },
  { name: 'Contact us', link: '#', type: '' },
  { name: 'Invite new members', link: '#', type: '' },
];

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
            path="/dashboard"
            component={MarketAppDashboard}
            auth={true}
          />
          <Route path="/sign-up">
            <MarketAppSignUps />
          </Route>
          <Route path="/item-id">
            <MarketAppTopMenu menu={menu} />
            <MarketAppItemDetails />
          </Route>
          <Route path="/">
            <MarketAppTopMenu menu={menu} />
            <MarketAppLandingPage />
          </Route>
          {/* <Redirect to="/sign-in" /> */}
        </Switch>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
