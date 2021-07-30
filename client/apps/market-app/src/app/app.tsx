import React, { useEffect, useState } from 'react';
import styles from './app.module.scss';
import { Route, Switch, Redirect, useLocation } from 'react-router-dom';

import { MarketAppLandingPage } from 'libs/market-app/landing-page/src/index';
import {
  MarketAppSignIn,
  selectSignInStateLoaded,
} from 'libs/market-app/sign-in/src/index';
import { MarketAppSignUps } from 'libs/market-app/sign-ups/src/index';
import { MarketAppItemDetails } from 'libs/market-app/item-details/src/index';
import { SharedAuthGuard } from 'libs/shared/auth-guard/src/index';
import { MarketAppDashboard } from 'libs/market-app/dashboard/src/index';
import { MarketAppTopMenu } from '@client/market-app/top-menu';
import { MarketAppSignOuts } from 'libs/market-app/sign-outs/src/index';
import { useSelector } from 'react-redux';

const menu = [
  { name: 'Home', link: '#', type: '' },
  { name: 'About', link: '#', type: '' },
  { name: 'Blog', link: '#', type: '' },
  { name: 'Contact us', link: '#', type: '' },
  { name: 'Invite new members', link: '#', type: '' },
];

/* eslint-disable-next-line */
export interface MarketAppProps {}

export function App(props: MarketAppProps) {
  const [isLogin, setIsLogin] = useState(false);
  const [routeLink, setRouteLink] = useState('');
  const { response } = useSelector(selectSignInStateLoaded);

  useEffect(() => {
    //check for admin right/privileges
    if (Object.entries(response).length > 0) {
      setIsLogin(true);
      setRouteLink('/dashboard/index');
    } else {
      setIsLogin(false);
      setRouteLink('/');
    }
  }, [response]);

  return (
    <Switch>
      <Route path="/sign-in">
        <MarketAppSignIn />
      </Route>

      <Route path="/sign-out">
        {/* <MarketAppTopMenu menu={menu} /> */}
        <MarketAppSignOuts />
      </Route>

      <Route path="/sign-up">
        <MarketAppSignUps />
      </Route>

      <Route path="/item-id">
        <MarketAppTopMenu menu={menu} />
        <MarketAppItemDetails />
      </Route>

      <SharedAuthGuard
        path="/dashboard/:slug"
        component={MarketAppDashboard}
        auth={isLogin}
      ></SharedAuthGuard>

      <Route exact path="/">
        <MarketAppTopMenu menu={menu} />
        <MarketAppLandingPage />
      </Route>

      <Redirect to={routeLink} />
    </Switch>
  );
}

export default App;
