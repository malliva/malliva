import React, { useEffect } from 'react';
import styles from './app.module.scss';
import {
  Route,
  BrowserRouter,
  Switch,
  Redirect,
  useRouteMatch,
} from 'react-router-dom';
import { Provider, useDispatch } from 'react-redux';
import { Store } from '@reduxjs/toolkit';

import { MarketAppLandingPage } from 'libs/market-app/landing-page/src/index';
import { MarketAppSignIn } from 'libs/market-app/sign-in/src/index';
import { MarketAppSignUps } from 'libs/market-app/sign-ups/src/index';
import { MarketAppItemDetails } from 'libs/market-app/item-details/src/index';
import { SharedAuthGuard } from 'libs/shared/auth-guard/src/index';
import { MarketAppDashboard } from 'libs/market-app/dashboard/src/index';
import { MarketAppTopMenu } from '@client/market-app/top-menu';
import { MarketAppSignOuts } from 'libs/market-app/sign-outs/src/index';

const menu = [
  { name: 'Home', link: '#', type: '' },
  { name: 'About', link: '#', type: '' },
  { name: 'Blog', link: '#', type: '' },
  { name: 'Contact us', link: '#', type: '' },
  { name: 'Invite new members', link: '#', type: '' },
];

export function App(props: { store: Store }) {
  useEffect(() => {
    console.log('test');
    //check for admin right/privileges
  }, []);
  return (
    <Provider store={props.store}>
      <BrowserRouter>
        <Switch>
          <Route exact path="/">
            <MarketAppTopMenu menu={menu} />
            <MarketAppLandingPage />
          </Route>
          <Route path="/sign-in">
            <MarketAppSignIn />
          </Route>
          <Route path="/sign-out">
            <MarketAppTopMenu menu={menu} />
            <MarketAppSignOuts />
          </Route>
          <Route path="/sign-up">
            <MarketAppSignUps />
          </Route>
          <Route path="/item-id">
            <MarketAppTopMenu menu={menu} />
            <MarketAppItemDetails />
          </Route>

          {/* Dashboard should be here */}
          <SharedAuthGuard
            path="/dashboard"
            component={MarketAppDashboard}
            auth={true}
          ></SharedAuthGuard>
          <Redirect to="/" />
        </Switch>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
