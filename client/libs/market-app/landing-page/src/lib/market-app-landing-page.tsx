import React from 'react';

import './market-app-landing-page.module.scss';

import { MarketAppTopMenu } from '@client/market-app/top-menu';
import { MarketAppMainFilter } from '@client/market-app/main-filter';
import { MarketAppItemList } from '@client/market-app/item-list';
import { MarketAppFooter } from '@client/market-app/footer';
import { MarketAppTopBanner } from '@client/market-app/top-banner';
import { MarketAppTopBarSettings } from '@client/market-app/top-bar-settings';
/* eslint-disable-next-line */
export interface MarketAppLandingPageProps {}

export function MarketAppLandingPage(props: MarketAppLandingPageProps) {
  return (
    <div>
      <MarketAppTopBanner />
      <div className="flex justify-center space-between flex-wrap">
        <MarketAppMainFilter />
        <MarketAppItemList />
      </div>

      <MarketAppFooter />
    </div>
  );
}

export default MarketAppLandingPage;
