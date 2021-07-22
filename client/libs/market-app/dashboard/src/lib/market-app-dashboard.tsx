import React from 'react';

import { MarketAppDashboardUi } from 'libs/market-app/dashboard/dashboard-ui/src/index';
import { MarketAppManageUsers } from 'libs/market-app/manage-users/src/index';
import { MarketAppDashboardDashboardMenu } from 'libs/market-app/dashboard/dashboard-menu/src/index';

import { MarketAppUserFields } from 'libs/market-app/user-fields/src/index';
import { MarketAppUserRights } from 'libs/market-app/user-rights/src/index';

import { MarketAppTopMenu } from '@client/market-app/top-menu';
import { Route, Switch, useRouteMatch } from 'react-router-dom';

/* eslint-disable-next-line */
export interface MarketAppDashboardProps {}

export function MarketAppDashboard(props: MarketAppDashboardProps) {
  const userNavigation = [{ name: 'Admin panel', href: '#', type: 'admin' }];
  const { path } = useRouteMatch();
  //Logout not working here yet Fix later
  return (
    <Switch>
      <Route path={`${path}/manage-users`}>
        <MarketAppTopMenu menu={userNavigation} />
        <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
          <MarketAppDashboardDashboardMenu />
          <MarketAppManageUsers />
        </div>
      </Route>
      <Route path={`${path}/users-rights`}>
        <MarketAppTopMenu menu={userNavigation} />
        <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
          <MarketAppDashboardDashboardMenu />
          <MarketAppUserRights />
        </div>
      </Route>
      <Route path={`${path}/users-fields`}>
        <MarketAppTopMenu menu={userNavigation} />
        <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
          <MarketAppDashboardDashboardMenu />
          <MarketAppUserFields />
        </div>
      </Route>
      <Route path={`${path}`}>
        <MarketAppTopMenu menu={userNavigation} />
        <div className="max-w-3xl mx-auto sm:px-6 lg:max-w-7xl lg:px-8 lg:grid lg:py-10 lg:grid-cols-12 lg:gap-8">
          <MarketAppDashboardDashboardMenu />
          <MarketAppDashboardUi />
        </div>
      </Route>
    </Switch>
  );
}

export default MarketAppDashboard;
